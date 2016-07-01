Name:       nfc-plugin-emul
Summary:    NFC emul plugin
Version:    0.0.16
Release:    0
Group:      TO_BE/FILLED_IN
License:    Apache-2.0
Source0:    %{name}-%{version}.tar.gz
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(vconf)
BuildRequires: pkgconfig(dlog)
BuildRequires: pkgconfig(nfc-common-lib)
BuildRequires: cmake
BuildRequires: gettext-tools

%description
NFC Plugin Emul

%prep
%setup -q


%build
cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix} \
%ifarch aarch64 x86_64
	-DTIZEN_ARCH_64=1 \
%endif

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

install -D -m 0644 LICENSE.Apache-2.0  %{buildroot}/%{_datadir}/license/nfc-plugin-emul

mkdir -p %{buildroot}%{_libdir}/udev/rules.d
cp 98-nfc-plugin-emul.rules %{buildroot}%{_libdir}/udev/rules.d/98-nfc-plugin-emul.rules

%postun -p /sbin/ldconfig

%post -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/nfc/libnfc-plugin.so
%{_datadir}/license/nfc-plugin-emul
%{_libdir}/udev/rules.d/98-nfc-plugin-emul.rules
