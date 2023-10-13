#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x579C160D4C9E23E8 (jelmer@jelmer.uk)
#
Name     : pypi-fastimport
Version  : 0.9.14
Release  : 13
URL      : https://files.pythonhosted.org/packages/7b/ab/c2d9bd0b7ae0956308be167b6e30f516edfeba3b34ebc1d7b96ce46dfe74/fastimport-0.9.14.tar.gz
Source0  : https://files.pythonhosted.org/packages/7b/ab/c2d9bd0b7ae0956308be167b6e30f516edfeba3b34ebc1d7b96ce46dfe74/fastimport-0.9.14.tar.gz
Source1  : https://files.pythonhosted.org/packages/7b/ab/c2d9bd0b7ae0956308be167b6e30f516edfeba3b34ebc1d7b96ce46dfe74/fastimport-0.9.14.tar.gz.asc
Summary  : VCS fastimport/fastexport parser
Group    : Development/Tools
License  : GPL-2.0
Requires: pypi-fastimport-bin = %{version}-%{release}
Requires: pypi-fastimport-license = %{version}-%{release}
Requires: pypi-fastimport-python = %{version}-%{release}
Requires: pypi-fastimport-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![Build Status](https://travis-ci.org/jelmer/python-fastimport.png?branch=master)](https://travis-ci.org/jelmer/python-fastimport)

%package bin
Summary: bin components for the pypi-fastimport package.
Group: Binaries
Requires: pypi-fastimport-license = %{version}-%{release}

%description bin
bin components for the pypi-fastimport package.


%package license
Summary: license components for the pypi-fastimport package.
Group: Default

%description license
license components for the pypi-fastimport package.


%package python
Summary: python components for the pypi-fastimport package.
Group: Default
Requires: pypi-fastimport-python3 = %{version}-%{release}

%description python
python components for the pypi-fastimport package.


%package python3
Summary: python3 components for the pypi-fastimport package.
Group: Default
Requires: python3-core
Provides: pypi(fastimport)

%description python3
python3 components for the pypi-fastimport package.


%prep
%setup -q -n fastimport-0.9.14
cd %{_builddir}/fastimport-0.9.14
pushd ..
cp -a fastimport-0.9.14 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672271506
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-fastimport
cp %{_builddir}/fastimport-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pypi-fastimport/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fast-import-filter
/usr/bin/fast-import-info
/usr/bin/fast-import-query

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-fastimport/06877624ea5c77efe3b7e39b0f909eda6e25a4ec

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
