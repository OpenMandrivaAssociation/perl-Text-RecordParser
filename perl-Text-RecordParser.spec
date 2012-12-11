%define upstream_name	 Text-RecordParser
%define upstream_version v1.5.0

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Read record-oriented files
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(IO::Scalar)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Readonly)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(version)

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{perl_vendorlib}/Text
%{_mandir}/man*/*


%changelog
* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 1.5.0-1mdv2011.0
+ Revision: 561551
- update to v1.5.0

* Thu Feb 18 2010 Jérôme Quelin <jquelin@mandriva.org> 1.4.0-1mdv2011.0
+ Revision: 507589
- update to 1.4.0

* Tue May 05 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.0-1mdv2010.0
+ Revision: 372188
- new version

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.2.1-3mdv2008.1
+ Revision: 140721
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.1-3mdv2008.0
+ Revision: 87026
- rebuild


* Sun Aug 13 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-13 17:48:18 (55814)
- Changed BuildRequires perl(version) to perl-version

* Sat Aug 12 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-12 15:51:30 (55750)
- Fixed BuildRequires

* Mon Aug 07 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-07 14:40:45 (53886)
- import perl-Text-RecordParser-1.2.1-1mdv2007.0

* Mon Aug 07 2006 Scott Karns <scottk@mandriva.org> 1.2.1-1mdv2007.0
- First Mandriva package

