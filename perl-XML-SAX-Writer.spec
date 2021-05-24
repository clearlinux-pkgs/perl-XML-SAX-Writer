#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-XML-SAX-Writer
Version  : 0.57
Release  : 20
URL      : https://cpan.metacpan.org/authors/id/P/PE/PERIGRIN/XML-SAX-Writer-0.57.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PE/PERIGRIN/XML-SAX-Writer-0.57.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libx/libxml-sax-writer-perl/libxml-sax-writer-perl_0.57-1.debian.tar.xz
Summary  : 'SAX2 XML Writer'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-XML-SAX-Writer-license = %{version}-%{release}
Requires: perl-XML-SAX-Writer-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(XML::Filter::BufferText)
BuildRequires : perl(XML::NamespaceSupport)
BuildRequires : perl(XML::SAX::Exception)

%description
This archive contains the distribution XML-SAX-Writer,
version 0.57:
SAX2 XML Writer

%package dev
Summary: dev components for the perl-XML-SAX-Writer package.
Group: Development
Provides: perl-XML-SAX-Writer-devel = %{version}-%{release}
Requires: perl-XML-SAX-Writer = %{version}-%{release}

%description dev
dev components for the perl-XML-SAX-Writer package.


%package license
Summary: license components for the perl-XML-SAX-Writer package.
Group: Default

%description license
license components for the perl-XML-SAX-Writer package.


%package perl
Summary: perl components for the perl-XML-SAX-Writer package.
Group: Default
Requires: perl-XML-SAX-Writer = %{version}-%{release}

%description perl
perl components for the perl-XML-SAX-Writer package.


%prep
%setup -q -n XML-SAX-Writer-0.57
cd %{_builddir}
tar xf %{_sourcedir}/libxml-sax-writer-perl_0.57-1.debian.tar.xz
cd %{_builddir}/XML-SAX-Writer-0.57
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/XML-SAX-Writer-0.57/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-XML-SAX-Writer
cp %{_builddir}/XML-SAX-Writer-0.57/LICENSE %{buildroot}/usr/share/package-licenses/perl-XML-SAX-Writer/555bcb759ba8c94f77eeced75b5a4d25c306afb0
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-XML-SAX-Writer/2f6e95209f8ad6bb846d76cb1b780d25075fd10a
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/XML::SAX::Writer.3
/usr/share/man/man3/XML::SAX::Writer::XML.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-XML-SAX-Writer/2f6e95209f8ad6bb846d76cb1b780d25075fd10a
/usr/share/package-licenses/perl-XML-SAX-Writer/555bcb759ba8c94f77eeced75b5a4d25c306afb0

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/XML/SAX/Writer.pm
/usr/lib/perl5/vendor_perl/5.34.0/XML/SAX/Writer/XML.pm
