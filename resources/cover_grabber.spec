%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary:    Download album cover art
Name:       cover_grabber
Version:    1.1.0
Release:    1%{?dist}
Source0:    http://69.164.204.114/cover_grabber-1.1.0.tar.gz
License:    GPLv3+
Group:      Applications/Multimedia
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:  noarch
URL:        https://sourceforge.net/projects/covergrabber/

BuildRequires: python-devel
Requires: python-mutagen

%description
Cover Grabber will recursively traverse a specified directory of media files 
and download album cover art from LastFM.  Very helpful if you have hundreds
or thousands of directories of music files.

* Currently supports mp3, ogg, and FLAC.

For instance:
$ covergrabber "/home/user/Music"

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.md README COPYING ChangeLog
%{_bindir}/covergrabber
%{python_sitelib}/cover_grabber/
%{python_sitelib}/cover_grabber-%{version}-py*.egg-info

%changelog
* Fri Dec 9 2011 Jayson Vaughn <vaughn.jayson@gmail.com> 1.1.0-1
- Added UTF-8 support
- Added dependency for mutagen in setup.py
* Thu Dec 8 2011 Jayson Vaughn <vaughn.jayson@gmail.com> 1.0.1-1
- Updated installation instructions
* Wed Dec 7 2011 Jayson Vaughn <vaughn.jayson@gmail.com> 1.0.0-1
- Added FLAC Support
- Added OGG Support
* Wed Dec 7 2011 Jayson Vaughn <vaughn.jayson@gmail.com> 0.0.2-2
- Changed spec file to adhere to Fedora package review (Bug #761063)
* Wed Dec 7 2011 Jayson Vaughn <vaughn.jayson@gmail.com> 0.0.2-1
- Initial RPM build
