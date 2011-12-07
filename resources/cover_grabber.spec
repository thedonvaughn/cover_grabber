%define name cover_grabber
%define version 0.0.2
%define unmangled_version 0.0.2
%define release 1

Summary: Recursively traverse a directory of mp3s downloading album cover art from LastFM
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://69.164.204.114/%{name}-%{unmangled_version}.tar.gz
License: GPL
Group: Application/Multimedia
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Requires: python-mutagen
Vendor: Jayson Vaughn <vaughn.jayson@gmail.com>
Packager: Jayson Vaughn <vaughn.jayson@gmail.com>
URL: http://github.com/thedonvaughn/cover_grabber

%description
Cover Grabber will recursively traverse a directory of mp3s and download album cover art from LastFM for all sub-directories.

%prep
%setup -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README.md README COPYING ChangeLog

%changelog
* Wed Dec 7 2011 Jayson Vaughn <vaughn.jayson at, gmail.com> 0.0.2-1
- Initial RPM build
