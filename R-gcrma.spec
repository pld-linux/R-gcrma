%define		packname	gcrma

Summary:	Background Adjustment Using Sequence Information
Name:		R-%{packname}
Version:	2.34.0
Release:	1
License:	LGPL
Group:		Applications/Engineering
Source0:	http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	44f0435123c2a962914dc6737d6881c2
Patch0:		bogus-deps.patch
URL:		http://www.bioconductor.org/packages/release/bioc/html/gcrma.html
BuildRequires:	R-Biobase >= 2.5.5
BuildRequires:	R
BuildRequires:	R-XVector-devel
BuildRequires:	texlive-latex
BuildRequires:	texinfo
Requires:	R-Biobase >= 2.5.5
Requires:	R
Requires:	R-XVector
Requires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Background adjustment using sequence information.

%prep
%setup -q -c -n %{packname}
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%dir %{_libdir}/R/library/%{packname}
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/NEWS
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/data
%dir %{_libdir}/R/library/gcrma/libs
%attr(755,root,root) %{_libdir}/R/library/gcrma/libs/gcrma.so
