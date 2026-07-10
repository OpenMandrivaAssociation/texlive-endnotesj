%global tl_name endnotesj
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.0
Release:	%{tl_revision}.1
Summary:	Japanese-style endnotes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/japanese/endnotesj
License:	bsd3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/endnotesj.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/endnotesj.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides customized styles for endnotes to be used with
Japanese documents. It can be used on pLaTeX, upLaTeX, and LuaLaTeX
(LuaTeX-ja).

