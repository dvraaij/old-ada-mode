# Upstream source information.
%global upstream_owner        dvraaij
%global upstream_name         old-ada-mode
%global upstream_version      4.0
%global upstream_commit_date  20240105
%global upstream_commit       c4e50f91eed91f76a4f9e278df320afe155e2246
%global upstream_shortcommit  %(c=%{upstream_commit}; echo ${c:0:7})

# Emacs package information.
%global pkg ada-mode

Name:           emacs-%{pkg}
Version:        %{upstream_version}^%{upstream_commit_date}git%{upstream_shortcommit}
Release:        1%{?dist}
Summary:        Emacs major mode for editing Ada source code
BuildArch:      noarch

License:        GPL-3.0-or-later AND GFDL-1.3-or-later

URL:            https://github.com/%{upstream_owner}/%{upstream_name}
Source0:        %{url}/archive/%{upstream_commit}.tar.gz#/%{upstream_name}-%{upstream_shortcommit}.tar.gz

BuildRequires:  emacs-nox
BuildRequires:  texinfo
BuildRequires:  texinfo-tex

Requires:       emacs(bin) >= %{_emacs_version}

%description
%{summary}.

The version in this package is based on ada-mode 4.0; the one that was
distributed with Emacs 27.1. It may be slow on very large files, but on the
other hand does not require an external parser as is the case for ada-mode
version 5.0 and later.


#############
## Prepare ##
#############

%prep
%autosetup -n %{upstream_name}-%{upstream_commit} -p1

# Remove precompiled documents.
rm doc/*.info
rm doc/*.html
rm doc/*.pdf


###########
## Build ##
###########

%build

# Byte-compile the Lisp-files.
%{_emacs_bytecompile} ada-*.el

# Build and install the documentation.
texi2any        -o doc/%{pkg}.info --no-split doc/%{pkg}.texi
texi2any --html -o doc/%{pkg}.html --no-split doc/%{pkg}.texi
texi2any --pdf  -o doc/%{pkg}.pdf  --no-split doc/%{pkg}.texi


#############
## Install ##
#############

%install

# Install Emacs-files.
install -dm 0755  %{buildroot}%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 ada-*.el* -t %{buildroot}%{_emacs_sitelispdir}/%{pkg}/

# Install the documentation.
mkdir --parents %{buildroot}%{_infodir}
install -pm 0644 doc/%{pkg}.info -t %{buildroot}%{_infodir}

mkdir --parents %{buildroot}%{_pkgdocdir}
install -pm 0644 doc/%{pkg}.html -t %{buildroot}%{_pkgdocdir}
install -pm 0644 doc/%{pkg}.pdf -t %{buildroot}%{_pkgdocdir}


###########
## Files ##
###########

%files
%license LICENSE
%doc README*
%{_emacs_sitelispdir}/%{pkg}
%{_infodir}/%{pkg}.info.*
%{_pkgdocdir}/%{pkg}.pdf
%{_pkgdocdir}/%{pkg}.html


###############
## Changelog ##
###############

%changelog
* Fri Jan 05 2024 Dennis van Raaij <dvraaij@fedoraproject.org> - 4.0^20240105gitc4e50f9-1
- New package.
