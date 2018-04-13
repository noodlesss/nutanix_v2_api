import json
import requests
 



class nutanixApi(object):
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password


#------ TESETS
########
    def get_vm_v1(self, vm_uuid):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.get(self.base_url + 'vms/%s' %vm_uuid, verify=False).json()
        return data

#------ Virtual Machine Operations  
########

    def get_vm_uuid(self, vm_name):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.get(self.base_url + 'vms', verify=False).json()
        for vm in data['entities']:
            if vm_name == vm['name']:
                return vm['uuid']
        return 'no such vm'

    def get_vm_list(self):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.get(self.base_url + 'vms', verify=False).json()
        return data


    def get_vm(self, vm_uuid):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.get(self.base_url + 'vms/%s' %vm_uuid, verify=False).json()
        return data


    def vm_create(self, body):
        '''body consist at least below parameters:
            {"memory_mb": 1024, "name": "pida","num_vcpus": 1}
        '''
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        print body
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.post(self.base_url + 'vms', json=body, verify=False).json()
        return data


    def vm_delete(self, vm_uuid):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.delete(self.base_url + 'vms/%s' %vm_uuid, verify=False).json()
        return data


    def vm_update(self, vm_uuid, body=None):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        try:
            data = s.put(self.base_url + 'vms/%s' %vm_uuid, json=body, verify=False).json()
        except Exception as e:
            print e
            data = s.put(self.base_url + 'vms/%s' %vm_uuid, json=body, verify=False)
        return data


    def vm_clone(self, vm_uuid, body=None):
        ''' body(optional) = clone machine parameters'''
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.post(self.base_url + 'vms/%s/clone' %vm_uuid, json=body, verify=False).json()
        return data


    def vm_disks_attach(self, vm_uuid, body):
        ''' body(required) = info about the virtual disks or CD-Roms to be attached. VDisk size, and storage_container_id 
        paramters are required.
        vdisk size should be in bytes'''
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.post(self.base_url + 'vms/%s/disks/attach' %vm_uuid, json=body, verify=False).json()
        return data


    def vm_disks_detach(self, vm_uuid, body):
        ''' body(required) = info about the virtual disks or CD-Roms to be detached. At least disk UUID or combination 
        of device index and adapter type must be provided.
        '''
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.post(self.base_url + 'vms/%s/disks/detach' %vm_uuid, json=body, verify=False).json()
        return data

    def vm_manage_guesttools(self, vm_uuid, body):
        ''' body(required) = Mount and unmount guest tools on a given Virtual Machine. 
            If override_guest is set to false and no empty CdRom is available on the guest VM, 
            then the mount operation will fail. If override_guest is set to true then the mount 
            operation succeeds by unmounting a non-empty CdRom.
        {
  "message": "Hypervisor ahv not supported",
  "detailed_message": "com.nutanix.prism.exception.vmmanagement.VMAdministrationException: com.nutanix.util.base.ValidationException: Hypervisor ahv not supported\n\tat com.nutanix.prism.services.v2.vmmanagement.VMAdministrationImpl.manageGuestTool(VMAdministrationImpl.java:238)\n\tat sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)\n\tat sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)\n\tat sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)\n\tat java.lang.reflect.Method.invoke(Method.java:498)\n\tat org.springframework.aop.support.AopUtils.invokeJoinpointUsingReflection(AopUtils.java:317)\n\tat org.springframework.aop.framework.ReflectiveMethodInvocation.invokeJoinpoint(ReflectiveMethodInvocation.java:190)\n\tat org.springframework.aop.framework.ReflectiveMethodInvocation.proceed(ReflectiveMethodInvocation.java:157)\n\tat org.springframework.security.access.intercept.aopalliance.MethodSecurityInterceptor.invoke(MethodSecurityInterceptor.java:64)\n\tat org.springframework.aop.framework.ReflectiveMethodInvocation.proceed(ReflectiveMethodInvocation.java:179)\n\tat org.springframework.aop.framework.JdkDynamicAopProxy.invoke(JdkDynamicAopProxy.java:207)\n\tat com.sun.proxy.$Proxy153.manageGuestTool(Unknown Source)\n\tat sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)\n\tat sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)\n\tat sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)\n\tat java.lang.reflect.Method.invoke(Method.java:498)\n\tat org.springframework.aop.support.AopUtils.invokeJoinpointUsingReflection(AopUtils.java:317)\n\tat org.springframework.aop.framework.ReflectiveMethodInvocation.invokeJoinpoint(ReflectiveMethodInvocation.java:190)\n\tat org.springframework.aop.framework.ReflectiveMethodInvocation.proceed(ReflectiveMethodInvocation.java:157)\n\tat com.nutanix.prism.aop.RequestInterceptor.invoke(RequestInterceptor.java:162)\n\tat org.springframework.aop.framework.ReflectiveMethodInvocation.proceed(ReflectiveMethodInvocation.java:179)\n\tat org.springframework.aop.framework.JdkDynamicAopProxy.invoke(JdkDynamicAopProxy.java:207)\n\tat com.sun.proxy.$Proxy267.manageGuestTool(Unknown Source)\n\tat sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)\n\tat sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)\n\tat sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)\n\tat java.lang.reflect.Method.invoke(Method.java:498)\n\tat org.apache.cxf.service.invoker.AbstractInvoker.performInvocation(AbstractInvoker.java:180)\n\tat org.apache.cxf.service.invoker.AbstractInvoker.invoke(AbstractInvoker.java:96)\n\tat org.apache.cxf.jaxrs.JAXRSInvoker.invoke(JAXRSInvoker.java:201)\n\tat org.apache.cxf.jaxrs.JAXRSInvoker.invoke(JAXRSInvoker.java:102)\n\tat org.apache.cxf.interceptor.ServiceInvokerInterceptor$1.run(ServiceInvokerInterceptor.java:58)\n\tat org.apache.cxf.interceptor.ServiceInvokerInterceptor.handleMessage(ServiceInvokerInterceptor.java:94)\n\tat org.apache.cxf.phase.PhaseInterceptorChain.doIntercept(PhaseInterceptorChain.java:271)\n\tat org.apache.cxf.transport.ChainInitiationObserver.onMessage(ChainInitiationObserver.java:121)\n\tat org.apache.cxf.transport.http.AbstractHTTPDestination.invoke(AbstractHTTPDestination.java:239)\n\tat org.apache.cxf.transport.servlet.ServletController.invokeDestination(ServletController.java:218)\n\tat org.apache.cxf.transport.servlet.ServletController.invoke(ServletController.java:163)\n\tat org.apache.cxf.transport.servlet.ServletController.invoke(ServletController.java:137)\n\tat org.apache.cxf.transport.servlet.CXFNonSpringServlet.invoke(CXFNonSpringServlet.java:158)\n\tat org.apache.cxf.transport.servlet.AbstractHTTPServlet.handleRequest(AbstractHTTPServlet.java:243)\n\tat org.apache.cxf.transport.servlet.AbstractHTTPServlet.doPost(AbstractHTTPServlet.java:163)\n\tat javax.servlet.http.HttpServlet.service(HttpServlet.java:648)\n\tat org.apache.cxf.transport.servlet.AbstractHTTPServlet.service(AbstractHTTPServlet.java:219)\n\tat org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:292)\n\tat org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:207)\n\tat org.apache.tomcat.websocket.server.WsFilter.doFilter(WsFilter.java:52)\n\tat org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:240)\n\tat org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:207)\n\tat com.nutanix.prism.web.filters.CacheControlFilter.doFilter(CacheControlFilter.java:44)\n\tat org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:240)\n\tat org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:207)\n\tat com.nutanix.prism.web.filters.ClusterUuidFilter.doFilterInternal(ClusterUuidFilter.java:46)\n\tat org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)\n\tat org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:240)\n\tat org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:207)\n\tat org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:330)\n\tat org.springframework.security.web.access.intercept.FilterSecurityInterceptor.invoke(FilterSecurityInterceptor.java:118)\n\tat org.springframework.security.web.access.intercept.FilterSecurityInterceptor.doFilter(FilterSecurityInterceptor.java:84)\n\tat org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)\n\tat org.springframework.security.web.access.ExceptionTranslationFilter.doFilter(ExceptionTranslationFilter.java:113)\n\tat org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)\n\tat org.springframework.security.web.session.SessionManagementFilter.doFilter(SessionManagementFilter.java:103)\n\tat org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)\n\tat org.springframework.security.web.servletapi.SecurityContextHolderAwareRequestFilter.doFilter(SecurityContextHolderAwareRequestFilter.java:154)\n\tat org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)\n\tat org.springframework.security.web.savedrequest.RequestCacheAwareFilter.doFilter(RequestCacheAwareFilter.java:45)\n\tat org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)\n\tat org.springframework.security.web.authentication.www.BasicAuthenticationFilter.doFilter(BasicAuthenticationFilter.java:150)\n\tat org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)\n\tat org.springframework.security.web.authentication.ui.DefaultLoginPageGeneratingFilter.doFilter(DefaultLoginPageGeneratingFilter.java:155)\n\tat org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)\n\tat org.springframework.security.web.authentication.AbstractAuthenticationProcessingFilter.doFilter(AbstractAuthenticationProcessingFilter.java:199)\n\tat org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)\n\tat org.springframework.web.filter.CompositeFilter$VirtualFilterChain.doFilter(CompositeFilter.java:107)\n\tat org.springframework.security.web.authentication.preauth.AbstractPreAuthenticatedProcessingFilter.doFilter(AbstractPreAuthenticatedProcessingFilter.java:94)\n\tat org.springframework.web.filter.CompositeFilter$VirtualFilterChain.doFilter(CompositeFilter.java:112)\n\tat org.springframework.security.web.authentication.preauth.AbstractPreAuthenticatedProcessingFilter.doFilter(AbstractPreAuthenticatedProcessingFilter.java:94)\n\tat org.springframework.web.filter.CompositeFilter$VirtualFilterChain.doFilter(CompositeFilter.java:112)\n\tat org.springframework.web.filter.CompositeFilter.doFilter(CompositeFilter.java:73)\n\tat org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)\n\tat org.springframework.security.web.authentication.preauth.AbstractPreAuthenticatedProcessingFilter.doFilter(AbstractPreAuthenticatedProcessingFilter.java:94)\n\tat org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)\n\tat org.springframework.security.web.authentication.logout.LogoutFilter.doFilter(LogoutFilter.java:110)\n\tat org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)\n\tat org.springframework.security.web.context.request.async.WebAsyncManagerIntegrationFilter.doFilterInternal(WebAsyncManagerIntegrationFilter.java:50)\n\tat org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)\n\tat org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)\n\tat org.springframework.security.web.authentication.preauth.AbstractPreAuthenticatedProcessingFilter.doFilter(AbstractPreAuthenticatedProcessingFilter.java:94)\n\tat org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)\n\tat org.springframework.security.web.context.SecurityContextPersistenceFilter.doFilter(SecurityContextPersistenceFilter.java:87)\n\tat org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)\n\tat org.springframework.security.web.FilterChainProxy.doFilterInternal(FilterChainProxy.java:192)\n\tat org.springframework.security.web.FilterChainProxy.doFilter(FilterChainProxy.java:160)\n\tat org.springframework.web.filter.DelegatingFilterProxy.invokeDelegate(DelegatingFilterProxy.java:344)\n\tat org.springframework.web.filter.DelegatingFilterProxy.doFilter(DelegatingFilterProxy.java:261)\n\tat org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:240)\n\tat org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:207)\n\tat com.thetransactioncompany.cors.CORSFilter.doFilter(CORSFilter.java:195)\n\tat com.thetransactioncompany.cors.CORSFilter.doFilter(CORSFilter.java:266)\n\tat org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:240)\n\tat org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:207)\n\tat org.apache.catalina.core.StandardWrapperValve.invoke(StandardWrapperValve.java:212)\n\tat org.apache.catalina.core.StandardContextValve.invoke(StandardContextValve.java:94)\n\tat org.apache.catalina.authenticator.AuthenticatorBase.invoke(AuthenticatorBase.java:504)\n\tat org.apache.catalina.core.StandardHostValve.invoke(StandardHostValve.java:141)\n\tat org.apache.catalina.valves.ErrorReportValve.invoke(ErrorReportValve.java:79)\n\tat org.apache.catalina.valves.AbstractAccessLogValve.invoke(AbstractAccessLogValve.java:620)\n\tat org.apache.catalina.core.StandardEngineValve.invoke(StandardEngineValve.java:88)\n\tat org.apache.catalina.connector.CoyoteAdapter.service(CoyoteAdapter.java:502)\n\tat org.apache.coyote.http11.AbstractHttp11Processor.process(AbstractHttp11Processor.java:1132)\n\tat org.apache.coyote.AbstractProtocol$AbstractConnectionHandler.process(AbstractProtocol.java:684)\n\tat org.apache.tomcat.util.net.NioEndpoint$SocketProcessor.doRun(NioEndpoint.java:1533)\n\tat org.apache.tomcat.util.net.NioEndpoint$SocketProcessor.run(NioEndpoint.java:1489)\n\tat java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)\n\tat java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)\n\tat org.apache.tomcat.util.threads.TaskThread$WrappingRunnable.run(TaskThread.java:61)\n\tat java.lang.Thread.run(Thread.java:748)\nCaused by: com.nutanix.util.base.ValidationException: Hypervisor ahv not supported\n\tat com.nutanix.prism.commands.AbstractCommand.checkHypervisorSupported(AbstractCommand.java:157)\n\tat com.nutanix.prism.commands.AbstractCommand.execute(AbstractCommand.java:124)\n\tat com.nutanix.prism.services.v2.vmmanagement.VMAdministrationImpl.manageGuestTool(VMAdministrationImpl.java:236)\n\t... 117 more\n",
  "error_code": {
    "code": 1101,
    "help_url": "http://my.nutanix.com"
  }
}
        '''

        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.post(self.base_url + 'vms/%s/manage_vm_guest_tools' %vm_uuid, json=body, verify=False).json()
        return data


    def vm_get_nics(self, vm_uuid, include_address_assignments=False):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.get(self.base_url + 'vms/%s/nics' %vm_uuid, params={"include_address_assignments": include_address_assignments} ,verify=False).json()
        return data


    def vm_add_nics(self, vm_uuid, body=None):
        '''network_uuid is required field'''
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.post(self.base_url + 'vms/%s/nics' %vm_uuid, json=body ,verify=False).json()
        return data


    def vm_update_nics(self, vm_uuid, nic_id, body=None):
        #couldn't update nic parameters through this func, or through Rest API Prism. 
        '''nic_id is mac address formated as xx-xx-xx-xx-xx-xx. network_uuid is required field'''
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        try:
            data = s.put(self.base_url + 'vms/%s/nics/%s' %(vm_uuid,nic_id), json=body ,verify=False).json()
        except Exception as e:
            print e
            data = s.put(self.base_url + 'vms/%s/nics/%s' %(vm_uuid, nic_id), json=body ,verify=False)
        return data


    def vm_restore(self, vm_uuid, body=None):
        '''snap_uuid is required field in body'''
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        try:
            data = s.post(self.base_url + 'vms/%s/restore' %(vm_uuid), json=body ,verify=False).json()
        except Exception as e:
            print e
            data = s.post(self.base_url + 'vms/%s/restore' %(vm_uuid), json=body ,verify=False)
        return data


    def vm_change_power_state(self, vm_uuid, power_state):
        power_state_list = { 'ON': 'ON', 'OFF': 'OFF', "POWERCYCLE": 'POWERCYCLE', "RESET": 'RESET',
      "PAUSE": 'PAUSE', "SUSPEND": 'SUSPEND', "RESUME": "RESUME",
      "ACPI_SHUTDOWN": "ACPI_SHUTDOWN", "ACPI_REBOOT": "ACPI_REBOOT"
             }
        if power_state not in power_state_list:
            return 'please choose power state from: %s' %power_state_list
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        body = {'transition': power_state}
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.post(self.base_url + 'vms/%s/set_power_state/' %vm_uuid, json=body, verify=False).json()
        #print data.text
        return data

    def vm_nics_del(self, vm_uuid, nic_id):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        try:
            data = s.delete(self.base_url + 'vms/%s/nics/%s' %(vm_uuid, nic_id), verify=False).json()
        except Exception as e:
            print e
            data = s.delete(self.base_url + 'vms/%s/nics/%s' %(vm_uuid, nic_id), verify=False)
            return data.text
        return data

    def vm_get_nic(self, vm_uuid, nic_id):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        try:
            data = s.get(self.base_url + 'vms/%s/nics/%s' %(vm_uuid, nic_id), verify=False).json()
        except Exception as e:
            print e
            data = s.get(self.base_url + 'vms/%s/nics/%s' %(vm_uuid, nic_id), verify=False)
            return data.text
        return data

#---------> Task Operations 
#####
    def get_task_status(self, task_id):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.get(self.base_url + 'tasks/%s' %task_id, verify=False).json()
        return data

    def get_tasks_list(self):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.post(self.base_url + 'tasks/list', verify=False).json()
        return data

    def get_tasks_poll(self):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.post(self.base_url + 'tasks/poll', verify=False).json()
        return data

#-----------> Snapshot Operations
#####
    def get_snapshots(self, vm_uuid=None):
        '''vm_uuid can be sent to see snapshots of vm'''
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        print vm_uuid
        data = s.get(self.base_url + 'snapshots/', params={'vm_uuid': vm_uuid}, verify=False).json()
        return data

    def delete_snapshots(self, snapshot_uuid):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.delete(self.base_url + 'snapshots/%s' %snapshot_uuid, verify=False).json()
        return data


    def get_snapshot_by_name(self, snapshot_name):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.get(self.base_url + 'snapshots/', verify=False).json()
        for snap in data['entities']:
            if snap.get('snapshot_name') == snapshot_name:
                return snap
        return 'no matching snapshot name found'

#-------------> Protection Domain Operations
#####
    def get_protection_domains(self):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        parameters = {"count": count}
        data = s.get(self.base_url + 'protection_domains/', verify=False).json()
        return data


    def get_protection_domain_snapshots(self, pd_name, count=10, filter_criteria=None, sort_criteria=None):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        parameters = {"count": count}
        try:
            data = s.get(self.base_url + 'protection_domains/%s/dr_snapshots' %pd_name, verify=False).json()
        except Exception as e:
            print e
            data = s.get(self.base_url + 'protection_domains/%s/dr_snapshots' %pd_name, verify=False)
        return data

    