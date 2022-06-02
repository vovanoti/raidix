Name:           raidix
Version:       1.0 
Release:        1%{?dist}
Summary:       This program just printing some text in STDOUT 

License:       GPL 
#URL:            
Source0:       raidix-1.0.tar.gz 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildRequires:  
#Requires:       

%description
A small program that just printing the text

%prep
%setup -q


%build
make

#%%configure
#make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp raidix $RPM_BUILD_ROOT/%{_bindir}

#%%make_install

%files
%defattr(-,root,root,-)
%{_bindir}/raidix
%doc



%changelog

%post
chmod 755 %{_bindir}/raidix 
