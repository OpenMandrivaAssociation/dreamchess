Summary:	OpenGL chess game
Name:		dreamchess
Version:	0.2.0
Release:	2
License:	GPLv3+
Group:		Games/Boards
Url:		http://www.dreamchess.org/
Source0:	%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}-48.png
Patch0:		dreamchess-0.2.0-pthread.patch
Patch1:		dreamchess-0.2.0-sfmt.patch
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(mxml)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(zlib)
Requires:	%{name}-data = %{EVRD}

%description
DreamChess is a user interface for playing chess. It comes with its own
engine called Dreamer. Both DreamChess and Dreamer are compatible with the
xboard/Winboard chess engine communication protocol. This means that
DreamChess can be used with other xboard-compatible chess engines such as
crafty (ftp://ftp.cis.uab.edu/pub/hyatt/) and GNU Chess
(http://www.gnu.org/software/chess/). Similarly, the Dreamer chess engine can
be used with other xboard-compatible user interfaces such as xboard and
Winboard (http://www.tim-mann.org/xboard.html) and recent editions of the
commercial chess program Chessmaster (http://www.chessmaster.com/).

%files
%doc README COPYING ChangeLog AUTHORS INSTALL
%{_gamesbindir}/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man6/*

#----------------------------------------------------------------------------

%package data
Summary:	Data files for DreamChess game
Group:		Games/Boards
BuildArch:	noarch
Requires:	%{name} = %{EVRD}

%description data
This package contains data files for DreamChess game.

%files data
%{_gamesdatadir}/*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure2_5x \
	--bindir=%{_gamesbindir} \
	--datadir=%{_gamesdatadir}
%make

%install
%makeinstall_std
install -pD -m644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -pD -m644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png

