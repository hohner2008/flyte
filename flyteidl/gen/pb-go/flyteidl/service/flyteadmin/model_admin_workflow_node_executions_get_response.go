/*
 * flyteidl/service/admin.proto
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * API version: version not set
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */

package flyteadmin

type AdminWorkflowNodeExecutionsGetResponse struct {
	Closure        *CoreCompiledWorkflowClosure `json:"closure,omitempty"`
	NodeExecutions []FlyteidladminNodeExecution `json:"node_executions,omitempty"`
}