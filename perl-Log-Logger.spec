%include	/usr/lib/rpm/macros.perl
%define		pdir	Log
%define		pnam	Logger
Summary:	Log::Logger perl module
Summary(pl.UTF-8):	Moduł perla Log::Logger
Name:		perl-Log-Logger
Version:	1.01
Release:	10
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	dbda4602f2eaad56472215d2734a6b6f
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log::Logger - OO interface to user defined logfile.

%description -l pl.UTF-8
Log::Logger - obiektowy interfejs do pliku logów użytkownika.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Log/Logger.pm
%{_mandir}/man3/*
