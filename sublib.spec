#
#
Summary:	SubLib is a library for managing movie subtitles
Summary(pl.UTF-8):	SubLib to biblioteka do obsługi napisów do filmów
Name:		sublib
Version:	0.9
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/sublib/%{name}-%{version}.zip
# Source0-md5:	8d09e2785b4a6fa62fba71e4169a51fe
Source1:	http://dl.sourceforge.net/sublib/%{name}-docs-%{version}.zip
# Source1-md5:	96a0e1e7f9ad71c9e97816725663a9c8
URL:		http://sublib.sourceforge.net/
BuildRequires:	mono-csharp
BuildRequires:	rpmbuild(monoautodeps)
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SubLib is a library for managing movie subtitles.

%description -l pl.UTF-8
SubLib to biblioteka do obsługi napisów do filmów.

%package devel
Summary:	Header files for SubLib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki SubLib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for SubLib library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki SubLib.

%prep
%setup -q -a1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/%{name}.dll

%files devel
%defattr(644,root,root,755)
%doc %{name}-docs-%{version}/docs/*
%{_pkgconfigdir}/*.pc
