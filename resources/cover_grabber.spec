%define name Cover Grabber
%define version 0.0.1
%define unmangled_version 0.0.1
%define release 1

Summary: Recursively traverse media directory and download album cover art
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: GNU GPL v3
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Jayson Vaughn <vaughn.jayson@gmail.com>
Url: http://github.com/thedonvaughn/cover_grabber

%description
Python application that will recurisvely traverse a directory of mp3s and download album cover art.
Currently the application uses LastFM to search for album covers.

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
