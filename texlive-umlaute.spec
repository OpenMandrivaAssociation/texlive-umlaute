%global tl_name umlaute
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1
Release:	%{tl_revision}.1
Summary:	German input encodings in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/umlaute
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/umlaute.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/umlaute.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/umlaute.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
An early package for using alternate input encodings. The author
considers the package mostly obsolete, since most of its functions are
taken by the inputenc package; however, inputenc doesn't support the
roman8 and atari encodings, so umlaute remains the sole source of that
support.

