%define upstream_name	 Text-RecordParser
%define upstream_version v1.5.0

Name:       perl-%{upstream_name}
Version:    %perl_convert_version 1.6.3
Release:    3

Summary:	Read record-oriented files

License:	GPL
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-v1.6.3.tar.gz

BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(IO::Scalar)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Readonly)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(JSON::PP)
BuildRequires:	perl(version)
BuildRequires: perl(Pod::Markdown)
BuildRequires: perl(Pod::Readme)
BuildRequires: perl(Text::Autoformat)

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
%setup -qn Text-RecordParser-v%{version}

%build
%{__perl} Build.PL installdirs=vendor
chmod a+w README.md
pwd
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%clean 

%files
%doc Changes README
%{_bindir}/tab*
%{perl_vendorlib}/Text
%{_mandir}/man*/*
