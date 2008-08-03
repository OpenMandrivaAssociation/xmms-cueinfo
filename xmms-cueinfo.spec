%define name xmms-cueinfo
%define version 0.2.0
%define release	%mkrel 8


Name:		%name
Summary:	Plugin for XMMS that adds support for reading cue files
Version:	%version
Release:	%release
Group:		Sound
License:	GPL
BuildRequires:	libxmms-devel glib-devel gtk+1.2-devel
Requires:	xmms
Url:		http://www.student.lu.se/~nbi98oli/xmms-cueinfo.html
Source:		%name-%version.tar.bz2
BuildRoot:	%_tmppath/%name-buildroot

%description
xmms-cueinfo is a plugin for XMMS that adds support for reading cue files. Cue
files describe what tracks a single audio file contains, including performer
and title information. This makes it possible to rip a full CD into a single
audio file. (The reason people do this is because of the audible gaps that
occur when the software switches between two files. However, these gaps are
generally shorter in unix-based operating systems than in Windows due to the
simpler file I/O subsystem. There are also no-gap plugins for many players now,
so there aren't really any good reasons for ripping CDs like this nowadays.)
xmms-cueinfo also makes it easy to seek to each track mentioned in the cue
file.

%prep
%setup -q

%build
%configure2_5x 
%make

%install
rm -rf %buildroot
%makeinstall libdir=%buildroot%{_libdir}/xmms/General/
rm -f %buildroot%{_libdir}/xmms/General/libcue_info.la

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc AUTHORS README TODO
%{_libdir}/xmms/General/libcue_info.so

