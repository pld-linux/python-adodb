%define		module	adodb
%define		ver	%(echo %{version} | tr -d . )
%define		postrel	b
#
Summary:	The Python version of ADOdb database library
Summary(pl.UTF-8):	Pythonowa wersja biblioteki bazodanowej ADOdb
Name:		python-%{module}
Version:	2.02
Release:	%{postrel}.0.1
License:	BSD-like
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/adodb/%{module}-py%{ver}%{postrel}.zip
# Source0-md5:	7b74550f68dcbd4e275ab2f1dda2c485
Patch0:		%{name}-setup.patch
URL:		http://phplens.com/lens/adodb/adodb-py-docs.htm
BuildRequires:	python-modules
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ADOdb is a database abstraction library (modelled on Microsoft's
database API's). ADOdb was originally developed for PHP, and ported to
Python. The Python version implements a subset of the PHP version.

%description -l pl.UTF-8
ADOdb to biblioteka abstrakcji baz danych modelowana na podstawie API
bazodanowego Microsoftu. ADOdb pierwotnie powstało w PHP i zostało
sportowane do Pythona. Wersja pythonowa implementuje podzbiór wersji w
PHP.

%prep
%setup -q -n %{module}-%{ver}
%patch0 -p1

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt adodb-py-docs.htm
%dir %{py_sitescriptdir}/adodb
%{py_sitescriptdir}/adodb/*.py[co]
%{py_sitescriptdir}/adodb-*.egg-info
