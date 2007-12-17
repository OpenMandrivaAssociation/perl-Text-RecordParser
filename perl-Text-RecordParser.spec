%define module	Text-RecordParser
%define name	perl-%{module}
%define	modprefix Text

%define	version	1.2.1
%define	rel	3
%define release %mkrel %{rel}

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
Summary:	Read record-oriented files
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-v%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(IO::Scalar)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Readonly)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
## perl-version doesn't seemt to provide perl(version)
BuildRequires:	perl-version
BuildArch:	noarch

%description
This module is for reading record-oriented data in a delimited text
file. The most common example have records separated by newlines and
fields separated by commas or tabs, but this module aims to provide a
consistent interface for handling sequential records in a file however
they may be delimited. Typically this data lists the fields in the
first line of the file, in which case you should call bind_header to
bind the field name (or not, and it will be called implicitly). If the
first line contains data, you can still bind your own field names via
bind_fields. Either way, you can then use many methods to get at the
data as arrays or hashes.

%prep
%setup -q -n %{module}-v%{version}

%build
%{__perl} Build.PL installdirs=vendor destdir=%{buildroot}
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_bindir}/tab*
%{perl_vendorlib}/%{modprefix}
%{_mandir}/man*/*






