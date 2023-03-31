%define oname colorama

Name:		python-%{oname}
Version:	0.4.4
Release:	3
Summary:	Cross-platform colored terminal text
Source0:	http://pypi.python.org/packages/source/c/%{oname}/%{oname}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://code.google.com/p/colorama/
BuildRequires:	dos2unix
BuildRequires:	python-setuptools
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

%prep
%autosetup -n %{oname}-%{version}
dos2unix README.rst


%build
%py_build

%install
%py_install

%files
%doc README.rst
%dir %{py_puresitedir}/colorama
%{py_puresitedir}/colorama/*.py*
%{py_puresitedir}/colorama*.egg-info
