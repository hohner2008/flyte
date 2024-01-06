/*
 * flyteidl/service/admin.proto
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * API version: version not set
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */

package flyteadmin

// InputData represents the inputs to a task or workflow. It's an envelope that contains a map of input variables to their values.
type CoreInputData struct {
	// A map of input variables to their values.
	Inputs *CoreLiteralMap `json:"inputs,omitempty"`
}