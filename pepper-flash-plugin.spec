%global debug_package %{nil}
%global pepperflash_path chromium-browser chromium

Name:           pepper-flash-plugin
Summary:        Chromium Flash player plugin
Version:        23.0.0.162
Release:        1%{?dist}

License:        Proprietary
Url:            http://www.google.com/chrome
Group:          Applications/Internet
Source0:        https://fpdownload.adobe.com/pub/flashplayer/pdc/%{version}/flash_player_ppapi_linux.i386.tar.gz
Source1:        https://fpdownload.adobe.com/pub/flashplayer/pdc/%{version}/flash_player_ppapi_linux.x86_64.tar.gz

BuildRequires:  rpm
BuildRequires:  cpio


%description
Pepper API based Adobe Flash plugin for Google's Open Source browser Chromium.


%prep
%setup -c -T


%build
%ifarch x86_64
    tar xaf %{SOURCE1}
%else
    tar xaf %{SOURCE0}
%endif


%install
mkdir -p %{buildroot}%{_libdir}/%{name}
install -m644 *.so *.json %{buildroot}%{_libdir}/%{name}/

%post
for ppf_path in %{pepperflash_path}
do
    ln -sf %{_libdir}/%{name}/libpepflashplayer.so %{_libdir}/$ppf_path/PepperFlash/libpepflashplayer.so &>/dev/null || :
    ln -sf %{_libdir}/%{name}/manifest.json %{_libdir}/$ppf_path/PepperFlash/manifest.json &>/dev/null || :
done

%postun
for ppf_path in %{pepperflash_path}
do
    rm -f %{_libdir}/$ppf_path/PepperFlash/libpepflashplayer.so &>/dev/null || :
    rm -f %{_libdir}/$ppf_path/PepperFlash/manifest.json &>/dev/null || :
done

%files
%{_libdir}/%{name}


%changelog
* Fri Oct 07 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 23.0.0.162-1
- Move widevinecdm-plugin to separate debug_package
