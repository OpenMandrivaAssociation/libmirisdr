%define major 4
%define libname %mklibname mirisdr %{major}
%define devname %mklibname -d mirisdr

Name:           libmirisdr
Version:        1.1.2
Release:        1%{?dist}
Summary:        Support programs for MRi2500
License:        GPL-2.0
Group:          Productivity/Hamradio/Other
Url:            https://github.com/f4exb/libmirisdr-4
Source0:	https://github.com/f4exb/libmirisdr-4/archive/v%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  pkgconfig(libusb)
BuildRequires:  pkgconfig(udev)

%description
Programs that controls Mirics MRi2500 based DVB dongle in raw mode, so
it can be used as a SDR receiver.

%package -n	%{libname}
Summary:        Libs libmirisdr
Group:          System/Libraries/C 

%description -n	%{libname}
Support programs for MRi2500

%package -n	%{devname}
Summary:        Development files for libmirisdr
Group:          Development/Libraries
Requires:	%{libname} = %{EVRD}

%description -n	%{devname}
Library headers and other development files for mirisdr driver.

%prep
%setup -q
sed -i 's!.x-xxx-xunknown!!g' cmake/Modules/Version.cmake

%build
%cmake
%make_build

%install
%make_install -C build
rm %{buildroot}%{_libdir}/libmirisdr.a

#install udev rules
install -D -p -m 0644 mirisdr.rules %{buildroot}%{_udevrulesdir}/10-mirisdr.rules

%files
%{_bindir}/miri_fm
%{_bindir}/miri_sdr
%{_udevrulesdir}/10-mirisdr.rules

%files -n %{libname}
%{_libdir}/libmirisdr.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING README
%{_libdir}/libmirisdr.so
%{_includedir}/mirisdr.h
%{_includedir}/mirisdr_export.h
%{_libdir}/pkgconfig/libmirisdr.pc
