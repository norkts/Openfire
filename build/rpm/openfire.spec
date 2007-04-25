Summary: Openfire XMPP Server
Name: openfire
Version: 3.3.0
Release: 1
BuildRoot: %{_builddir}/%{name}-root
Source0: %{name}_src_3_3_0.tar.gz
Group: Applications/Communications
Vendor: Jive Software
License: GPL
Requires: jdk >= 1.5.0
URL: http://www.igniterealtime.org/

%description
Openfire is a leading Open Source, cross-platform IM server based on the
XMPP (Jabber) protocol. It has great performance, is easy to setup and use,
and delivers an innovative feature set.

%prep

%build

%install
# There's no need to package this.
rm $RPM_BUILD_ROOT/opt/openfire/logs/stderr.out
# Set up the init script.
mkdir -p $RPM_BUILD_ROOT/etc/init.d
cp $RPM_BUILD_ROOT/opt/openfire/bin/extra/openfired $RPM_BUILD_ROOT/etc/init.d/openfired
chmod 755 $RPM_BUILD_ROOT/etc/init.d/openfired
# Make the startup script executable.
chmod 755 $RPM_BUILD_ROOT/opt/openfire/bin/openfire.sh
# Set up the sysconfig file.
#mkdir -p $RPM_BUILD_ROOT/etc/sysconfig
#cp $RPM_BUILD_ROOT/opt/openfire/bin/extra/openfire-sysconfig $RPM_BUILD_ROOT/etc/sysconfig/openfire

%pre
if /usr/bin/id jive > /dev/null 2>&1 ; then
	: # user already exists
else
	/usr/sbin/groupadd -r jive
	/usr/sbin/useradd -r -g jive -d /opt/openfire -s /bin/bash -c "jive" jive
	/usr/sbin/usermod -G jive jive
fi

%post
/sbin/chkconfig --add openfired

%files
%defattr(-,jive,jive)
%dir /opt/openfire
/opt/openfire/bin
%dir /opt/openfire/conf
%config(noreplace) /opt/openfire/conf/openfire.xml
/opt/openfire/lib
%dir /opt/openfire/logs
/opt/openfire/plugins
%dir /opt/openfire/resources
/opt/openfire/resources/database
/opt/openfire/resources/i18n
/opt/openfire/resources/nativeAuth
/opt/openfire/resources/spank
%dir /opt/openfire/resources/security
%config(noreplace) /opt/openfire/resources/security/keystore
%config(noreplace) /opt/openfire/resources/security/truststore
%doc /opt/openfire/documentation
%doc /opt/openfire/LICENSE.html 
%doc /opt/openfire/README.html 
%doc /opt/openfire/changelog.html
/etc/init.d/openfired
%config(noreplace) /etc/sysconfig/openfire