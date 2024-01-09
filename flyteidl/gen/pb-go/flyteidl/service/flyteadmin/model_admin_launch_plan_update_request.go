/*
 * flyteidl/service/admin.proto
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * API version: version not set
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */

package flyteadmin

type AdminLaunchPlanUpdateRequest struct {
	// Identifier of launch plan for which to change state. +required.
	Id *CoreIdentifier `json:"id,omitempty"`
	// Desired state to apply to the launch plan. +required.
	State *AdminLaunchPlanState `json:"state,omitempty"`
}