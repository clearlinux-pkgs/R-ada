#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ada
Version  : 2.0.5
Release  : 12
URL      : https://cran.r-project.org/src/contrib/ada_2.0-5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ada_2.0-5.tar.gz
Summary  : The R Package Ada for Stochastic Boosting
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : buildreq-R

%description
logistic loss on a given data set.  The package ada provides a straightforward, 
             well-documented, and broad boosting routine for classification, ideally suited 
             for small to moderate-sized data sets.

%prep
%setup -q -c -n ada
cd %{_builddir}/ada

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640964713

%install
export SOURCE_DATE_EPOCH=1640964713
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ada
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ada
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ada
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc ada || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ada/DESCRIPTION
/usr/lib64/R/library/ada/INDEX
/usr/lib64/R/library/ada/Meta/Rd.rds
/usr/lib64/R/library/ada/Meta/data.rds
/usr/lib64/R/library/ada/Meta/features.rds
/usr/lib64/R/library/ada/Meta/hsearch.rds
/usr/lib64/R/library/ada/Meta/links.rds
/usr/lib64/R/library/ada/Meta/nsInfo.rds
/usr/lib64/R/library/ada/Meta/package.rds
/usr/lib64/R/library/ada/NAMESPACE
/usr/lib64/R/library/ada/R/ada
/usr/lib64/R/library/ada/R/ada.rdb
/usr/lib64/R/library/ada/R/ada.rdx
/usr/lib64/R/library/ada/data/datalist
/usr/lib64/R/library/ada/data/soldat.rda
/usr/lib64/R/library/ada/help/AnIndex
/usr/lib64/R/library/ada/help/ada.rdb
/usr/lib64/R/library/ada/help/ada.rdx
/usr/lib64/R/library/ada/help/aliases.rds
/usr/lib64/R/library/ada/help/paths.rds
/usr/lib64/R/library/ada/html/00Index.html
/usr/lib64/R/library/ada/html/R.css
