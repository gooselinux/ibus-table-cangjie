Name:       ibus-table-cangjie
Version:    1.2.0.20100210
Release:    1%{?dist}
Summary:    Cang Jie and derived tables for IBus-Table
License:    GPLv3
Group:      System Environment/Libraries
URL:        http://code.google.com/p/ibus/
Source0:    http://cloud.github.com/downloads/kaio/ibus-table-cangjie/%{name}-%{version}.tar.gz

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

Requires:         ibus >= 1.2, ibus-table >= 1.2.0.20100111-2
Requires(post):   ibus >= 1.2, ibus-table >= 1.2.0.20100111-2
BuildRequires:    ibus >= 1.2, ibus-table-devel >= 1.2.0.20100111-2

%description
The package contains Cang Jie and derived tables for IBus-Table, namely Cang 
Jie 3, Cang Jie 5, Cang Jie (big), Speed Cang Jie 6, Quick 3, Quick 5, Quick 
Classic, Easy (big).

%prep
%setup -q

%build
export IBUS_TABLE_CREATEDB="%{_bindir}/ibus-table-createdb -o"
%configure \
    --prefix=%{_prefix} \
    --enable-cangjie3 \
    --enable-cangjie5 \
    --enable-cangjiebig \
    --enable-scj6 \
    --enable-quick3 \
    --enable-quick5 \
    --enable-quickclassic \
    --enable-easybig
%__make %{?_smp_mflags}

%install
%__rm -rf %{buildroot}
%__make DESTDIR=%{buildroot} NO_INDEX=true INSTALL="install -p" install

%clean
%__rm -rf %{buildroot}

%post
cd %{_datadir}/ibus-table/tables/
%{_bindir}/ibus-table-createdb -i -n cangjie3.db
%{_bindir}/ibus-table-createdb -i -n cangjie5.db
%{_bindir}/ibus-table-createdb -i -n cangjie-big.db
%{_bindir}/ibus-table-createdb -i -n scj6.db
%{_bindir}/ibus-table-createdb -i -n quick3.db
%{_bindir}/ibus-table-createdb -i -n quick5.db
%{_bindir}/ibus-table-createdb -i -n quick-classic.db
%{_bindir}/ibus-table-createdb -i -n easy-big.db

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%verify(not md5 size mtime) %{_datadir}/ibus-table/tables/cangjie3.db
%verify(not md5 size mtime) %{_datadir}/ibus-table/tables/cangjie5.db
%verify(not md5 size mtime) %{_datadir}/ibus-table/tables/cangjie-big.db
%verify(not md5 size mtime) %{_datadir}/ibus-table/tables/scj6.db
%verify(not md5 size mtime) %{_datadir}/ibus-table/tables/quick3.db
%verify(not md5 size mtime) %{_datadir}/ibus-table/tables/quick5.db
%verify(not md5 size mtime) %{_datadir}/ibus-table/tables/quick-classic.db
%verify(not md5 size mtime) %{_datadir}/ibus-table/tables/easy-big.db
%{_datadir}/ibus-table/icons/cangjie3.svg
%{_datadir}/ibus-table/icons/cangjie5.svg
%{_datadir}/ibus-table/icons/cangjie-big.png
%{_datadir}/ibus-table/icons/scj6.svg
%{_datadir}/ibus-table/icons/quick3.png
%{_datadir}/ibus-table/icons/quick5.png
%{_datadir}/ibus-table/icons/quick-classic.png
%{_datadir}/ibus-table/icons/easy-big.png

%changelog
* Mon Feb 15 2010 Caius 'kaio' Chance <cchance at redhat.com> - 1.2.0.20100210-1
- Resolves: rhbz#559807
- Updates from upstream.
- Wraps description.

* Fri Feb 12 2010 Caius 'kaio' Chance <cchance at redhat.com> - 1.2.0.20100119-8
- Resolves: rhbz#559807
- Change BuildRequires from ibus-table to ibus-table-devel, as .pc is moved.

* Fri Feb 12 2010 Caius 'kaio' Chance <cchance at redhat.com> - 1.2.0.20100119-7
- Resolves: rhbz#559807
- build with noarch

* Fri Feb 12 2010 Caius 'kaio' Chance <cchance at redhat.com> - 1.2.0.20100119-6
- Resolves: rhbz#559807
- rebuilt

* Mon Feb 08 2010 Caius 'kaio' Chance <cchance at redhat.com> - 1.2.0.20100119-5
- Resolves: rhbz#559807
- rebuilt

* Fri Feb 05 2010 Caius 'kaio' Chance <cchance at redhat.com> - 1.2.0.20100119-4
- Resolves: rhbz#559807
- Removed Arch: noarch.

* Fri Jan 29 2010 Caius 'kaio' Chance <cchance at redhat.com> - 1.2.0.20100119-3
- Resolves: rhbz#559807
- rebuilt

* Fri Jan 29 2010 Caius 'kaio' Chance <cchance at redhat.com> - 1.2.0.20100119-2
- Resolves: rhbz#559807
- rebuilt

* Fri Jan 29 2010 Caius 'kaio' Chance <cchance at redhat.com> - 1.2.0.20100119-1
- Resolves: rhbz#559807
- Updated source from upstream.

* Mon Aug 31 2009 Caius 'kaio' Chance <k AT kaio.me> - 1.2.0.20090831-2.fc12
- Typo in file section.

* Mon Aug 31 2009 Caius 'kaio' Chance <k AT kaio.me> - 1.2.0.20090831-1.fc12
- Updated source.
- Added CangJie (big) table.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.20090717-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Caius 'kaio' Chance <k AT kaio.me> - 1.2.0.20090717-5.fc12
- Rebuilt.

* Wed Jul 22 2009 Caius 'kaio' Chance <k AT kaio.me> - 1.2.0.20090717-4.fc12
- Removed unneccessary BuildRequires.
- Removed unneccessary owned directories.
- Changed autogen.sh into configure.

* Mon Jul 20 2009 Caius 'kaio' Chance <k AT kaio.me> - 1.2.0.20090717-3.fc12
- Rebuilt.

* Fri Jul 17 2009 Caius 'kaio' Chance <k AT kaio.me> - 1.2.0.20090717-2.fc12
- Updated file list.

* Fri Jul 17 2009 Caius 'kaio' Chance <k AT kaio.me> - 1.2.0.20090717-1.fc12
- Rebuilt with IBus 1.2.

* Fri Jul 03 2009 Caius 'kaio' Chance <k AT kaio.me> - 1.1.0.20090309-12.fc12
- Rebuilt.

* Wed Jul 01 2009 Caius 'kaio' Chance <k AT kaio.me> - 1.1.0.20090309-11.fc12
- Rebuilt with ibus-table 1.2.0.

* Wed Jul 01 2009 Caius 'kaio' Chance <k AT kaio.me> - 1.1.0.20090309-10.fc12
- Fixed that change into table directory for index creation.
- Added owned directories in file section.
- Removed bootstrap.
- Updated package dependencies.

* Mon May 18 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090309-9.fc12
- Rebuilt with no index during install, index creation during post-install.

* Mon May 18 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090309-8.fc12
- Resolves: rhbz#500973 (Missing .txt during post.)

* Thu Apr 23 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090309-7.fc12
- Refined file properties and updated description.

* Fri Mar 13 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090309-6.fc11
- Created Public Domain statement in for tables.

* Fri Mar 13 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090309-5.fc11
- Labelled changes of checksum of db files during post-install stage.
- Moved COPYING to icons for more accurate license coverage.
- Required ibus-table at post-install stage.

* Thu Mar 12 2009 Jens Petersen <petersen@redhat.com> - 1.1.0.20090309-4
- actually do --no-create-index to half size of binary package

* Thu Mar 12 2009 Jens Petersen <petersen@redhat.com> - 1.1.0.20090309-3
- add bcond for bootstrap
- add back automake and gettext BRs
- macro usage fixes

* Thu Mar 12 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090309-2.fc11
- Resolves: rhbz#488010
- Added index creation of Cangjie 3, Cangjie 5, Quick 3, Quick 5 at post-
  installation stage.

* Tue Mar 10 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090309-1.fc11
- Resolves: rhbz#488010
- Update sources tarball to 1.1.0-20090309.
- Removed usage of 'configure' and db creation replaced by usage of autogen.sh.

* Mon Mar  9 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090220-4.fc11
- Resolves: rhbz#488010
- Corrected license declaration.

* Fri Mar  6 2009 Jens Petersen <petersen@redhat.com> - 1.1.0.20090220-3
- ibus-table.pc now fixed so don't need to patch
- configure with cangjie3
- fix paths in post script

* Fri Mar 06 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090220-2.fc11
- Resolves: rhbz#488010
- Added "BuildReq" automake.
- Corrected license version to GPLv3.

* Mon Mar 02 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090220-1.fc11
- Resolves: rhbz#488010
- Splited from ibus-table.
