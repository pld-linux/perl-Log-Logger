%include	/usr/lib/rpm/macros.perl
%define	pdir	Log
%define	pnam	Logger
Summary:	Log::Logger perl module
Summary(pl):	Modu³ perla Log::Logger
Name:		perl-Log-Logger
Version:	1.01
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log::Logger - OO interface to user defined logfile.

%description -l pl
Log::Logger - obiektowy interfejs do pliku logów u¿ytkownika.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Log/Logger.pm
%{_mandir}/man3/*
