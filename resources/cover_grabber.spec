%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary: Download album cover art
Name: cover_grabber
Version: 0.0.2
Release: 1%{?dist}
Source0: http://69.164.204.114/cover_grabber-0.0.2.tar.gz
License: GPLv3+
Group: Applications/Multimedia
BuildRoot: %{_tmppath}/cover_grabber-0.0.2-1-buildroot
BuildArch: noarch
URL: http://github.com/thedonvaughn/cover_grabber

BuildRequires: python-devel
Requires: python-mutagen

%description
Cover Grabber will recursively traverse a specified directory of mp3s 
and download album cover art from LastFM.

For instance:
$ covergrabber "/home/user/Music"

%prep
%setup -q cover_grabber-0.0.2

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root-)
%doc README.md README COPYING ChangeLog
%{_bindir}/covergrabber
%{python_sitelib}/cover_grabber/
%{python_sitelib}/cover_grabber-%{version}-py*.egg-info

%changelog
* Wed Dec 7 2011 Jayson Vaughn <vaughn.jayson at, gmail.com> 0.0.2-1
- Initial RPM build
