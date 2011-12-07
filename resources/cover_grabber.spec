%define name cover_grabber
%define version 0.0.1
%define unmangled_version 0.0.1
%define release 1

Summary: Recursively traverse directory of MP3s and download album cover art from LastFM
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: GPL
Group: Application/Multimedia
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Requires: python-mutagen
Vendor: Jayson Vaughn <vaughn.jayson@gmail.com>
Url: http://github.com/thedonvaughn/cover_grabber

%description
Cover Grabber will recursively traverse a directory of mp3s and download album cover art from LastFM.

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
