%define 	module	ordereddict
Summary:	Drop-in substitute for Py2.7's new collections.OrderedDict
Name:		python-%{module}
Version:	1.1
Release:	1
License:	MIT
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/o/ordereddict/%{module}-%{version}.tar.gz
# Source0-md5:	a0ed854ee442051b249bfad0f638bbec
URL:		http://pypi.python.org/pypi/ordereddict
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Drop-in substitute for Py2.7's new collections.OrderedDict that works
in Python 2.4-2.6. The recipe has big-oh performance that matches
regular dictionaries (amortized O(1) insertion/deletion/lookup and
O(n) iteration/repr/copy/equality_testing).

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%{py_sitescriptdir}/%{module}.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif
