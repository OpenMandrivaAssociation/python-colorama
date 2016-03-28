%define	oname	colorama

Name:		python-%{oname}
Version:	0.3.7
Release:	1
Summary:	Cross-platform colored terminal text
Source0:	http://pypi.python.org/packages/source/c/%{oname}/%{oname}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://code.google.com/p/colorama/
BuildRequires:	dos2unix
BuildRequires:	python-setuptools
BuildRequires:	python2-setuptools
BuildArch:	noarch

%description
Makes ANSI escape character sequences, for producing colored terminal text and
cursor positioning, work under MS Windows.

ANSI escape character sequences have long been used to produce colored terminal
text and cursor positioning on Unix and Macs. Colorama makes this work on
Windows, too. It also provides some shortcuts to help generate ANSI sequences,
and works fine in conjunction with any other ANSI sequence generation library,
such as Termcolor (http://pypi.python.org/pypi/termcolor.)

This has the upshot of providing a simple cross-platform API for printing
colored terminal text from Python, and has the happy side-effect that existing
applications or libraries which use ANSI sequences to produce colored output on
Linux or Macs can now also work on Windows, simply by calling
``colorama.init()``.

%package -n python2-colorama
Summary:	Cross-platform colored terminal text
Group:		Development/Python

%description -n python2-colorama
Makes ANSI escape character sequences, for producing colored terminal text and
cursor positioning, work under MS Windows.

ANSI escape character sequences have long been used to produce colored terminal
text and cursor positioning on Unix and Macs. Colorama makes this work on
Windows, too. It also provides some shortcuts to help generate ANSI sequences,
and works fine in conjunction with any other ANSI sequence generation library,
such as Termcolor (http://pypi.python.org/pypi/termcolor.)

This has the upshot of providing a simple cross-platform API for printing
colored terminal text from Python, and has the happy side-effect that existing
applications or libraries which use ANSI sequences to produce colored output on
Linux or Macs can now also work on Windows, simply by calling
``colorama.init()``.

%prep
%setup -q -n %{oname}-%{version}
dos2unix README.rst

cp -a . %py2dir

%build
pushd %py2dir
python2 setup.py build
popd

python setup.py build

%install
pushd %py2dir
python2 setup.py install --root=%{buildroot}
popd

python setup.py install --root=%{buildroot}

%files
%doc README.rst
%{py_puresitedir}/colorama/*.py*
%{py_puresitedir}/colorama*.egg-info

%files -n python2-colorama
%doc README.rst
%{py2_puresitedir}/colorama/*.py*
%{py2_puresitedir}/colorama*.egg-info

