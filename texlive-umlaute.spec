# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/umlaute
# catalog-date 2009-10-10 17:55:02 +0200
# catalog-license lppl
# catalog-version v2.1
Name:		texlive-umlaute
Version:	v2.1
Release:	3
Summary:	German input encodings in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/umlaute
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/umlaute.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/umlaute.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/umlaute.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> v2.1-2
+ Revision: 757251
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> v2.1-1
+ Revision: 719841
- texlive-umlaute
- texlive-umlaute
- texlive-umlaute

