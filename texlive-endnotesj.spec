Name:		texlive-endnotesj
Version:	47703
Release:	1
Summary:	Japanese-style endnotes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/endnotesj
License:	bsd3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/endnotesj.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/endnotesj.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides customized styles for endnotes to be used
with Japanese documents. It can be used on pLaTeX, upLaTeX, and
LuaLaTeX (LuaTeX-ja).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/endnotesj
%doc %{_texmfdistdir}/doc/latex/endnotesj

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
