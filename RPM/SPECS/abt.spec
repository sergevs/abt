Name:       abt
Version:    3.1.2
Release:    ssv1%{?dist}
Summary:    abt is advanced building system tool
License:    BSD
Group:	    Development/Tools
BuildArch:  noarch
Requires:   rpm-build redhat-rpm-config rpmdevtools subversion sudo yum-utils tar curl sed ed git
Source:	    %name-%version.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%version-buildroot

%description
the tool can be used to organize arbitrary command's flows
and provides basic log/debug functions for command execution
it contain all function to build from svn using rpmbuild and mock

%prep
%setup 

%build

%install
%__rm -rf %buildroot
%__mkdir_p %buildroot%_bindir
%__mkdir_p %buildroot/etc/abt
%__install abt %buildroot%_bindir
%__install abtrc abt.functions %buildroot/etc/abt
%__cp -a mock %buildroot/etc/abt

%files
%defattr(-,root,root)
%_bindir/*
%dir /etc/abt/
/etc/abt/abt.functions
%config(noreplace) /etc/abt/abtrc
%dir /etc/abt/mock
%config(noreplace) /etc/abt/mock

%changelog
* Thu Sep 19 2013 Serge <abrikus@gmail.com> 2.0.1.3-ssv1
- Initial public release
