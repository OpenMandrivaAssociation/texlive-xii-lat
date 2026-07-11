%global tl_name xii-lat
%global tl_revision 45805

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Christmas silliness (Latin)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/contrib/xii-lat
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xii-lat.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xii-lat.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is the plain TeX file xii-lat.tex. Call "pdftex xii-lat.tex" to
produce a (perhaps) surprising typeset document.

