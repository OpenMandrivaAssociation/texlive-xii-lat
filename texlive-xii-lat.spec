Name:		texlive-xii-lat
Version:	45805
Release:	1
Summary:	Christmas silliness (Latin)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xii-lat
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xii-lat.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xii-lat.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is the plain TeX file xii-lat.tex. Call "pdftex
xii-lat.tex" to produce a (perhaps) surprising typeset
document.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/plain/xii-lat

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
