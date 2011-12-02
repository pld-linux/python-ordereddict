#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define 	module	ordereddict
Summary:	-
Summary(pl.UTF-8):	-
Name:		python-%{module}
Version:	1.1
Release:	0.1
License:	- (enter GPL/GPL v2/GPL v3/LGPL/BSD/BSD-like/other license name here)
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/o/ordereddict/%{module}-%{version}.tar.gz
# Source0-md5:	a0ed854ee442051b249bfad0f638bbec
URL:		http://pypi.python.org/pypi/ordereddict
# remove BR: python-devel for 'noarch' packages.
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
#Requires:		python-libs
Requires:		python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif
