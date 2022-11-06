Summary:	OpenGL chess game
Name:		dreamchess
Version:	0.3.0
Release:	1
License:	GPLv3+
Group:		Games/Boards
Url:		http://www.dreamchess.org/
Source0:	https://github.com/dreamchess/dreamchess/archive/refs/tags/0.3.0.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}-48.png
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(mxml)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(SDL2_image)
BuildRequires:	pkgconfig(SDL2_mixer)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	cmake ninja

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
%{_bindir}/*
%{_datadir}/icons/*/*/*/*.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_mandir}/man6/*
%doc %{_docdir}/DreamChess

%prep
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
#install -pD -m644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
