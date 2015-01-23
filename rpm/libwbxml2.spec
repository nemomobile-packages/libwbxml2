Name: libwbxml2
Version: 0.10.8+git2
Release: 1
Summary: Library to parse, encode and handle WBXML documents
Group: System/Libraries
License: LGPLv2.1
Source0: %{name}-%{version}.tar.gz
BuildRequires: expat-devel zlib-devel popt-devel
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: cmake

%description
The WBXML Library (aka libwbxml) contains a library and its associated
tools to Parse, Encode and Handle WBXML documents.  The WBXML format
is a binary representation of XML, defined by the Wap Forum, and used
to reduce bandwidth in mobile communications.


%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_libdir}/*.so.*
%doc %{_docdir}/*

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
%{summary}.

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%prep
%setup -q -n %{name}-%{version}

%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr ..
make


%install
rm -rf %{buildroot}
make -C build DESTDIR=%{buildroot} install
rm -rf build

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
