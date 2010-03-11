#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	ExtUtils
%define	pnam	CChecker
Summary:	ExtUtils::CChecker - configure-time utilities for using C headers, libraries, or OS features
#Summary(pl.UTF-8):
Name:		perl-ExtUtils-CChecker
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/P/PE/PEVANS/ExtUtils-CChecker-%{version}.tar.gz
# Source0-md5:	f2a9da32e70ec32c5b47652e020021d0
URL:		http://search.cpan.org/dist/ExtUtils-CChecker/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-Pod
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Often Perl modules are written to wrap functionallity found in
existing C headers, libraries, or to use OS-specific features. It is
useful in the Build.PL or Makefile.PL file to check for the existance
of these requirements before attempting to actually build the module.

Objects in this class provide an extension around ExtUtils::CBuilder
to simplify the creation of a .c file, compiling, linking and running
it, to test if a certain feature is present.

It may also be necessary to search for the correct library to link
against, or for the right include directories to find header files in.
This class also provides assistance here.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/ExtUtils/CChecker.pm
%{_mandir}/man3/*.3pm*
