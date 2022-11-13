Name:		texlive-umlaute
Version:	15878
Release:	1
Summary:	German input encodings in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/umlaute
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/umlaute.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/umlaute.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/umlaute.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
An early package for using alternate input encodings. The
author considers the package mostly obsolete, since most of its
functions are taken by the inputenc package; however, inputenc
doesn't support the roman8 and atari encodings, so umlaute
remains the sole source of that support.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/umlaute/atari.def
%{_texmfdistdir}/tex/latex/umlaute/isolatin.def
%{_texmfdistdir}/tex/latex/umlaute/mac.def
%{_texmfdistdir}/tex/latex/umlaute/pc850.def
%{_texmfdistdir}/tex/latex/umlaute/roman8.def
%{_texmfdistdir}/tex/latex/umlaute/umlaute.sty
%doc %{_texmfdistdir}/doc/latex/umlaute/cs_patch.uue
%doc %{_texmfdistdir}/doc/latex/umlaute/umlaute.pdf
#- source
%doc %{_texmfdistdir}/source/latex/umlaute/umlaute.dtx
%doc %{_texmfdistdir}/source/latex/umlaute/umlaute.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
