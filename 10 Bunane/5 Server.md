## Frp
/opt/frp

## drawDB
```shell
docker pull hub.rat.dev/xinsodev/drawdb  ##加上代理hub.rat.dev
docker run -d --name drawdb --restart always -p 3316:80 hub.rat.dev/xinsodev/drawdb
```
# minio

```shell
docker run -p 9000:9000 -p 9090:9090 \
     --name minio \
     -d --restart=always \
     -e "MINIO_ACCESS_KEY=admin" \
     -e "MINIO_SECRET_KEY=QfnU1024." \
     -v /home/qfnu/bzw/minio/data:/data \
     -v /home/qfnu/bzw/minio/config:/root/.minio \
     minio/minio:RELEASE.2023-04-28T18-11-17Z server \
     /data --console-address ":9090" -address ":9000"
```

# Jenkins

```shell
sudo mkdir -p /opt/jenkins/jenkins_home
sudo mkdir -p /opt/jenkins/logs
sudo mkdir -p /opt/jenkins/docker
sudo chmod 777 /opt/jenkins



# 0b4cb832a6ef4f4f8ece2fb578cca93c
docker run -p 10008:8080 -p 10009:5000 --name jenkins \
--restart=always -u root \
-v /opt/jenkins/jenkins_home:/var/jenkins_home \
-v /opt/jenkins/logs:/var/logs \
-v /opt/jenkins/docker:/var/docker \
-v /var/run/docker.sock:/var/run/docker.sock \
-d jenkins/jenkins:lts

docker exec -it jenkins /bin/bash
cat /var/jenkins_home/secrets/initialAdminPassword
```

# Sonarqube
```shell
docker run  -itd  --name sonarqube \
    -p 10033:9000 \
    -v /opt/sonarqube/conf:/opt/sonarqube/conf \
    -v /opt/sonarqube/extensions:/opt/sonarqube/extensions \
    -v /opt/sonarqube/logs:/opt/sonarqube/logs \
    -v /opt/sonarqube/data:/opt/sonarqube/data \
	sonarqube:25.10.0.114319-community
```
admin:Xu1SiDao1024.
# Ldap
```
XUES1Dao1024.
```

```shell
cd /var/www/
sudo mkdir ldap && cd ldap
sudo mkdir -p data/slapd/database data/slapd/config secrets
sudo vim docker-compose.yml
```

```yaml
services:
  ldap:
    image: osixia/openldap:1.5.0
    container_name: openldap
    hostname: openldap
    environment:
      TZ: Asia/Shanghai
      LDAP_ORGANISATION: "xuesidao.com"
      LDAP_DOMAIN: "xuesidao.com"
      LDAP_ADMIN_USERNAME: "admin"
      LDAP_ADMIN_PASSWORD: "BUnana1024."
      LDAP_TLS: "false"
      LDAP_REPLICATION: "false"
    volumes:
      - ./data/slapd/database:/var/lib/ldap
      - ./data/slapd/config:/etc/ldap/slapd.d
      - ./data/openldap/certs:/container/service/slapd/assets/certs
    ports:
      - "389:389"
    restart: always
    networks:
      - ldap-net

  ldap-admin:
    image: osixia/phpldapadmin:latest
    container_name: phpldapadmin
    hostname: phpldapadmin
    environment:
      TZ: Asia/Shanghai
      PHPLDAPADMIN_LDAP_HOSTS: "openldap"
      PHPLDAPADMIN_HTTPS: "false"
    ports:
      - "10031:80"
    depends_on:
      - ldap
    restart: always
    networks:
      - ldap-net

networks:
  ldap-net:
    driver: bridge
```

```shell
docker compose down
docker compose up -d
```
## 修改管理员密码
https://www.cnblogs.com/ophui/p/16524174.html

### 1 查看管理员密码的字段
```shell
docker exec -it openldap bash
ldapsearch -H ldapi:// -LLL -Q -Y EXTERNAL -b "cn=config" "(olcRootDN=*)" dn olcRootDN olcRootPW
```
### 2 设置openldap管理员新密码
```
slappasswd -s "test123456"
sudo vim newpasswd.ldif
```
### 3 添加新密码文件newpasswd.ldif
```newpasswd.ldif
dn: olcDatabase={1}mdb,cn=config
changetype: modify
replace: olcRootPW
olcRootPW: {SSHA}nPZRGouNPUXKv6nh4DOqF5SFNgTh9aF9
```
### 4 使用ldapmodify命令导入上述文件
```shell
cd /etc/ldap/slapd.d/
ldapmodify -H ldapi:// -Y EXTERNAL -f newpasswd.ldif
```

## 自助修改密码
```shell
sudo touch /var/www/ssp/ssp.conf.php
docker run -p 10032:80 \
    --name ssp \
    -d --restart=always \
    -v /var/www/ssp/ssp.conf.php:/var/www/conf/config.inc.local.php \
    -v /var/www/ssp/images:/var/www/htdocs/images/custom \
    -v /var/www/ssp/zh-CN.inc.php:/var/www/lang/zh-CN.inc.php \
    docker.io/ltbproject/self-service-password:latest
```

```shell
docker stop ssp
docker rm ssp
```

```shell
docker exec -it ssp /bin/bash
```
修改路径：/usr/share/self-service-password/images下的图片
其中logo.png为logo图片，background.jpeg为背景图片


```php
<?php
#==============================================================================
# LTB Self Service Password
#
# Copyright (C) 2009 Clement OUDOT
# Copyright (C) 2009 LTB-project.org
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# GPL License: http://www.gnu.org/licenses/gpl.txt
#
#==============================================================================

#==============================================================================
# Configuration
#==============================================================================
# LDAP
$ldap_url = "ldap://202.194.176.103:389";
$ldap_starttls = false;
$ldap_binddn = "cn=admin,dc=xuesidao,dc=com";
$ldap_bindpw = "test123456";
$ldap_base = "dc=xuesidao,dc=com";

$ldap_login_attribute = "cn";
$ldap_fullname_attribute = "cn";
$ldap_filter = "(&(objectClass=person)($ldap_login_attribute={login}))";

# Active Directory mode
# true: use unicodePwd as password field
# false: LDAPv3 standard behavior
$ad_mode = false;
# Force account unlock when password is changed
$ad_options['force_unlock'] = false;
# Force user change password at next login
$ad_options['force_pwd_change'] = false;
# Allow user with expired password to change password
$ad_options['change_expired_password'] = false;

# Samba mode
# true: update sambaNTpassword and sambaPwdLastSet attributes too
# false: just update the password
$samba_mode = false;
# Set password min/max age in Samba attributes
#$samba_options['min_age'] = 5;
#$samba_options['max_age'] = 45;

# Shadow options - require shadowAccount objectClass
# Update shadowLastChange
$shadow_options['update_shadowLastChange'] = false;

# Hash mechanism for password:
# SSHA
# SHA
# SMD5
# MD5
# CRYPT
# clear (the default)
# auto (will check the hash of current password)
# This option is not used with ad_mode = true
$hash = "SSHA";

# Prefix to use for salt with CRYPT
$hash_options['crypt_salt_prefix'] = "$6$";

# Local password policy
# This is applied before directory password policy
# Minimal length
$pwd_min_length = 6;
# Maximal length
$pwd_max_length = 16;
# Minimal lower characters
$pwd_min_lower = 1;
# Minimal upper characters
$pwd_min_upper = 1;
# Minimal digit characters
$pwd_min_digit = 1;
# Minimal special characters
$pwd_min_special = 0;
# Definition of special characters
$pwd_special_chars = "^a-zA-Z0-9";
# Forbidden characters
#$pwd_forbidden_chars = "@%";
# Don't reuse the same password as currently
$pwd_no_reuse = true;
# Check that password is different than login
$pwd_diff_login = true;
# Complexity: number of different class of character required
$pwd_complexity = 0;
# Show policy constraints message:
# always
# never
# onerror
$pwd_show_policy = "never";
# Position of password policy constraints message:
# above - the form
# below - the form
$pwd_show_policy_pos = "above";

# Who changes the password?
# Also applicable for question/answer save
# user: the user itself
# manager: the above binddn
$who_change_password = "user";

## Standard change
# Use standard change form?
$use_change = true;

## Questions/answers
# Use questions/answers?
# true (default)
# false
$use_questions = false;

# Answer attribute should be hidden to users!
$answer_objectClass = "extensibleObject";
$answer_attribute = "info";

# Extra questions (built-in questions are in lang/$lang.inc.php)
#$messages['questions']['ice'] = "What is your favorite ice cream flavor?";

## Token
# Use tokens?
# true (default)
# false
$use_tokens = true;
# Crypt tokens?
# true (default)
# false
$crypt_tokens = true;
# Token lifetime in seconds
$token_lifetime = "3600";

## Mail
# LDAP mail attribute
$mail_attribute = "mail";
# Who the email should come from
$mail_from = "544207374@qq.com";
$mail_from_name = "消息-自助账号密码服务";
# Notify users anytime their password is changed
$notify_on_change = true;
# PHPMailer configuration (see https://github.com/PHPMailer/PHPMailer)
$mail_sendmailpath = '/usr/sbin/sendmail';
$mail_protocol = 'smtp';
$mail_smtp_debug = 0;
$mail_debug_format = 'error_log';
$mail_smtp_host = 'smtp.qq.com';
$mail_smtp_auth = true;
$mail_smtp_user = '544207374@qq.com';
$mail_smtp_pass = '';
$mail_smtp_port = 465;
$mail_smtp_timeout = 30;
$mail_smtp_keepalive = false;
$mail_smtp_secure = 'ssl';
$mail_contenttype = 'text/plain';
$mail_charset = 'utf-8';
$mail_priority = 3;
$mail_newline = PHP_EOL;

## SMS
# Use sms
$use_sms = false;
# GSM number attribute
$sms_attribute = "mobile";
# Partially hide number
$sms_partially_hide_number = true;
# Send SMS mail to address
$smsmailto = "{sms_attribute}@service.provider.com";
# Subject when sending email to SMTP to SMS provider
$smsmail_subject = "Provider code";
# Message
$sms_message = "{smsresetmessage} {smstoken}";

# SMS token length
$sms_token_length = 6;

# Max attempts allowed for SMS token
$max_attempts = 3;

# Reset URL (if behind a reverse proxy)
#$reset_url = $_SERVER['HTTP_X_FORWARDED_PROTO'] . "://" . $_SERVER['HTTP_X_FORWARDED_HOST'] . $_SERVER['SCRIPT_NAME'];

# Display help messages
$show_help = true;

# Language
$lang ="cn";

# Display menu on top
$show_menu = true;

# Logo
# $logo = "images/logo.png";

# Background image
$background_image = "images/background.jpg";

# Debug mode
$debug = false;

# Encryption, decryption keyphrase
$keyphrase = "speedbotchangepasswd";

# Where to log password resets - Make sure apache has write permission
# By default, they are logged in Apache log
#$reset_request_log = "/var/log/self-service-password";

# Invalid characters in login
# Set at least "*()&|" to prevent LDAP injection
# If empty, only alphanumeric characters are accepted
$login_forbidden_chars = "*()&|";

## CAPTCHA
# Use Google reCAPTCHA (http://www.google.com/recaptcha)
$use_recaptcha = false;
# Go on the site to get public and private key
$recaptcha_publickey = "";
$recaptcha_privatekey = "";
# Customization (see https://developers.google.com/recaptcha/docs/display)
$recaptcha_theme = "light";
$recaptcha_type = "image";
$recaptcha_size = "normal";

## Default action
# change
# sendtoken
# sendsms
$default_action = "change";

## Extra messages
# They can also be defined in lang/ files
#$messages['passwordchangedextramessage'] = NULL;
#$messages['changehelpextramessage'] = NULL;

# Launch a posthook script after successful password change
#$posthook = "/usr/share/self-service-password/posthook.sh";

?>
```

# Git
```
admin
WUZBGG9wCp7YHzS
```