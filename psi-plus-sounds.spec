%define rev 20110924gita883f82

Name:           psi-plus-sounds
Version:        0.15
Release:        0.1.%{rev}%{?dist}.R
Epoch:          1
BuildArch:      noarch
Summary:        Sounds for Psi+

License:        Unknown
URL:            http://code.google.com/p/psi-dev/
Source0:        %{name}-%{version}-20110924gita883f82.tar.gz
Source1:        generate-tarball.sh

BuildRequires:  tar
Requires:       psi-plus >= 1:0.15-0.20.20110919git5117.R

%description
This package contains sounds for Psi+.

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/psi-plus/
%{__tar} xzf %{SOURCE0} -C $RPM_BUILD_ROOT%{_datadir}/psi-plus/

%files
%defattr(-,root,root,-)
%{_datadir}/psi-plus/sound/*

%changelog
* Sun Oct 09 2011 Ivan Romanov <drizt@land.ru> - 1:0.15-0.1.20110924gita883f82.R
- Fixed revision

* Sun Oct 09 2011 Ivan Romanov <drizt@land.ru> - 0.15-0.120110924gita883f82.R
- Initial version of package
