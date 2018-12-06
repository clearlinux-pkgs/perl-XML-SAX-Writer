#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-XML-SAX-Writer
Version  : 0.57
Release  : 8
URL      : https://cpan.metacpan.org/authors/id/P/PE/PERIGRIN/XML-SAX-Writer-0.57.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PE/PERIGRIN/XML-SAX-Writer-0.57.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libx/libxml-sax-writer-perl/libxml-sax-writer-perl_0.57-1.debian.tar.xz
Summary  : 'SAX2 XML Writer'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-XML-SAX-Writer-license = %{version}-%{release}
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

%description dev
dev components for the perl-XML-SAX-Writer package.


%package license
Summary: license components for the perl-XML-SAX-Writer package.
Group: Default

%description license
license components for the perl-XML-SAX-Writer package.


%prep
%setup -q -n XML-SAX-Writer-0.57
cd ..
%setup -q -T -D -n XML-SAX-Writer-0.57 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/XML-SAX-Writer-0.57/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-XML-SAX-Writer
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-XML-SAX-Writer/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-XML-SAX-Writer/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.1/XML/SAX/Writer.pm
/usr/lib/perl5/vendor_perl/5.28.1/XML/SAX/Writer/XML.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/XML::SAX::Writer.3
/usr/share/man/man3/XML::SAX::Writer::XML.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-XML-SAX-Writer/LICENSE
/usr/share/package-licenses/perl-XML-SAX-Writer/deblicense_copyright
