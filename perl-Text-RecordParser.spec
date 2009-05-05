%define module	Text-RecordParser
%define name	perl-%{module}
%define	modprefix Text
%define	version	1.3.0
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
Summary:	Read record-oriented files
Url:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Text/%{module}-%{version}.tar.gz
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(IO::Scalar)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Readonly)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-version
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_bindir}/tab*
%{perl_vendorlib}/%{modprefix}
%{_mandir}/man*/*






