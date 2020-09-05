Summary:	Tools for working with the PinePhone hardware
Name:		pinephone-tools
Version:	1.0
Release:	0.20200905.1
Url:		https://xnux.eu/devices/feature/audio-pp.html
# Tools to drive PinePhone hardware...
# Audio routing
Source0:	https://xnux.eu/devices/feature/call-audio.c
# Modem
# See https://xnux.eu/devices/feature/modem-pp.html#toc-modem-power-driver
# for documentation on the driver
Source1:	modem
# Unlock adb access to the modem
Source2:	https://xnux.eu/devices/feature/qadbkey-unlock.c
# Systemd integration for the modem...
Source3:	modem.service
Source4:	modem-wait-powered.service
# ALSA configurations
Source10:	https://raw.githubusercontent.com/dreemurrs-embedded/Pine64-Arch/master/PKGBUILDS/pine64/alsa-ucm-pinephone/HiFi.conf
Source11:	https://raw.githubusercontent.com/dreemurrs-embedded/Pine64-Arch/master/PKGBUILDS/pine64/alsa-ucm-pinephone/PinePhone.conf
Source12:	https://raw.githubusercontent.com/dreemurrs-embedded/Pine64-Arch/master/PKGBUILDS/pine64/alsa-ucm-pinephone/VoiceCall.conf
#ExclusiveArch:	aarch64
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(libxcrypt)
License:	GPLv3+

%description
Tool to set up audio routing on the PinePhone

%prep

%build
%{__cc} %{optflags} -o pinephone-audio-setup %{S:0}
%{__cc} %{optflags} -o modem-adb-access %{S:2} -lcrypt

%install
mkdir -p %{buildroot}%{_bindir}
cp pinephone-audio-setup modem-adb-access %{S:1} %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_datadir}/alsa/ucm2
cp %{S:10} %{S:11} %{S:12} %{buildroot}%{_datadir}/alsa/ucm2/

mkdir -p %{buildroot}/lib/systemd/system
cp %{S:3} %{S:4} %{buildroot}/lib/systemd/system/

%files
%{_bindir}/pinephone-audio-setup
%{_bindir}/modem
%{_bindir}/modem-adb-access
%{_datadir}/alsa/ucm2/*.conf
/lib/systemd/system/modem.service
/lib/systemd/system/modem-wait-powered.service
