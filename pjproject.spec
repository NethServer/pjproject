Summary: PJSIP is a free and open source multimedia communication library
Name: pjproject
Version: 2.5.5
Release: 1%{dist}
License: GPL
Group: Utilities/System
Source0: http://www.pjsip.org/release/%{version}/%{name}-%{version}.tar.bz2
Patch0: 0001-pjlib-config_site_h.patch
Patch1: user.mak.diff
BuildRoot: %{_tmppath}/%{name}-%{version}-root
URL: http://pjsip.org/
BuildRequires: gsm-devel
BuildRequires: libsrtp-devel
BuildRequires: speex-devel
BuildRequires: openssl-devel
Requires: gsm
Requires: libsrtp
Requires: speex
Requires: openssl

%description
PJSIP is a free and open source multimedia communication library

%package devel
Summary: Libraries and header files for pjproject development
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: gsm-devel
Requires: libsrtp-devel
Requires: speex-devel

%description devel
The static libraries and header files needed for building additional plugins/modules

%prep
%setup -n %{name}-%{version}
%patch0 -p 1
%patch1 -p 0

%build
%{configure} --enable-shared --with-external-speex --with-external-gsm --with-external-srtp --disable-sound --disable-resample
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%post
ldconfig

%clean
cd $RPM_BUILD_DIR
%{__rm} -rf %{name}-%{version}
%{__rm} -rf /var/log/%{name}-sources-%{version}-%{release}.make.err
%{__rm} -rf $RPM_BUILD_ROOT

%files
#
#  Module List
#
%defattr(-, root, root)
%{_libdir}/libpj.so
%{_libdir}/libpj.so.2
%{_libdir}/libpjlib-util.so
%{_libdir}/libpjlib-util.so.2
%{_libdir}/libpjmedia.so
%{_libdir}/libpjmedia.so.2
%{_libdir}/libpjmedia-audiodev.so
%{_libdir}/libpjmedia-audiodev.so.2
%{_libdir}/libpjmedia-codec.so
%{_libdir}/libpjmedia-codec.so.2
%{_libdir}/libpjmedia-videodev.so
%{_libdir}/libpjmedia-videodev.so.2
%{_libdir}/libpjnath.so
%{_libdir}/libpjnath.so.2
%{_libdir}/libpjsip.so
%{_libdir}/libpjsip.so.2
%{_libdir}/libpjsip-simple.so
%{_libdir}/libpjsip-simple.so.2
%{_libdir}/libpjsip-ua.so
%{_libdir}/libpjsip-ua.so.2
%{_libdir}/libpjsua.so
%{_libdir}/libpjsua.so.2
%{_libdir}/libpjsua2.so
%{_libdir}/libpjsua2.so.2
%{_libdir}/libg7221codec.so
%{_libdir}/libg7221codec.so.2
%{_libdir}/libilbccodec.so
%{_libdir}/libilbccodec.so.2
%{_includedir}/pjsua2.hpp
%{_includedir}/pjsua2/*
%{_libdir}/libpjsua2.so
%{_libdir}/libpjsua2.so.2

%files devel
#
#  Header Files
#
%defattr(-, root, root)
%dir %{_includedir}/pj/
%dir %{_includedir}/pj/compat/
%{_includedir}/pj/*.h
%{_includedir}/pj/compat/*.h
%{_includedir}/pj/compat/*.h.in
%dir %{_includedir}/pj++/
%{_includedir}/pj++/*.hpp
%dir %{_includedir}/pjlib-util/
%{_includedir}/pjlib-util/*.h
%dir %{_includedir}/pjmedia/
%{_includedir}/pjmedia/*.h
%{_includedir}/pjmedia/*.h.in
%dir %{_includedir}/pjmedia-audiodev/
%{_includedir}/pjmedia-audiodev/*.h
%dir %{_includedir}/pjmedia-codec/
%{_includedir}/pjmedia-codec/*.h
%{_includedir}/pjmedia-codec/*.h.in
%dir %{_includedir}/pjmedia-videodev/
%{_includedir}/pjmedia-videodev/*.h
%dir %{_includedir}/pjnath/
%{_includedir}/pjnath/*.h
%dir %{_includedir}/pjsip/
%{_includedir}/pjsip/*.h
%{_includedir}/pjsip/*.h.in
%dir %{_includedir}/pjsip-simple/
%{_includedir}/pjsip-simple/*.h
%dir %{_includedir}/pjsip-ua/
%{_includedir}/pjsip-ua/*.h
%dir %{_includedir}/pjsua-lib/
%{_includedir}/pjsua-lib/*.h

%{_includedir}/pjlib.h
%{_includedir}/pjlib++.hpp
%{_includedir}/pjlib-util.h
%{_includedir}/pjmedia_audiodev.h
%{_includedir}/pjmedia_videodev.h
%{_includedir}/pjmedia-codec.h
%{_includedir}/pjmedia.h
%{_includedir}/pjnath.h
%{_includedir}/pjsip.h
%{_includedir}/pjsip_auth.h
%{_includedir}/pjsip_simple.h
%{_includedir}/pjsip_ua.h
%{_includedir}/pjsua.h

%{_libdir}/*

%changelog
* Tue Apr 29 2014 Derek Carter <derek.carter@schmoozecom.com> 2.2-9
- Adding patches of user.mak and pjlib-config_site_h

* Mon Apr 28 2014 Derek Carter <derek.carter@schmoozecom.com> 2.2-7
- updated format for new global makefile
