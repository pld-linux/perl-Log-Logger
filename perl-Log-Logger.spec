%include	/usr/lib/rpm/macros.perl
Summary:	Log-Logger perl module
Summary(pl):	Modu³ perla Log-Logger
Name:		perl-Log-Logger
Version:	1.01
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Log/Log-Logger-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log-Logger - OO interface to user defined logfile.

%description -l pl
Log-Logger - obiektowy interfejs do pliku logów u¿ytkownika.

%prep
%setup -q -n Log-Logger-%{version}

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
