# Copyright 2015 Internap.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import warnings


class BackwardCompatibleSwitchOperations(object):
    """
    Depecrated methods
    """
    def remove_access_vlan(self, interface_id):
        warnings.warn("Deprecated, use unset_interface_access_vlan(interface_id) instead")
        return self.unset_interface_access_vlan(interface_id)

    def configure_native_vlan(self, interface_id, vlan):
        warnings.warn("Deprecated, use set_interface_native_vlan(interface_id, vlan) instead")
        return self.set_interface_native_vlan(interface_id, vlan)

    def remove_native_vlan(self, interface_id):
        warnings.warn("Deprecated, use unset_interface_native_vlan(interface_id) instead")
        return self.unset_interface_native_vlan(interface_id)

    def remove_vlan_access_group(self, vlan_number, direction):
        warnings.warn("Deprecated, use unset_vlan_access_group(vlan_number, direction) instead")
        return self.unset_vlan_access_group(vlan_number, direction)

    def remove_vlan_vrf(self, vlan_number):
        warnings.warn("Deprecated, use unset_vlan_vrf(vlan_number) instead")
        return self.unset_vlan_vrf(vlan_number)

    def remove_interface_description(self, interface_id):
        warnings.warn("Deprecated, use unset_interface_description(interface_id) instead")
        return self.unset_interface_description(interface_id)

    def edit_interface_spanning_tree(self, interface_id):
        warnings.warn("Deprecated, use set_interface_spanning_tree_state(interface_id, edge=None) instead")
        return self.set_interface_spanning_tree_state(interface_id)

    def remove_bond_description(self, number):
        warnings.warn("Deprecated, use unset_bond_description(number) instead")
        return self.unset_bond_description(number)

    def configure_bond_native_vlan(self, number, vlan):
        warnings.warn("Deprecated, use set_bond_native_vlan(number, vlan) instead")
        return self.set_bond_native_vlan(number, vlan)

    def remove_bond_native_vlan(self, number):
        warnings.warn("Deprecated, use unset_bond_native_vlan(number) instead")
        return self.unset_bond_native_vlan(number)

    def edit_bond_spanning_tree(self, number, edge=None):
        warnings.warn("Deprecated, use set_bond_interface_spanning_tree_state(number, edge=None) instead")
        return self.set_bond_interface_spanning_tree_state(number)

    def enable_lldp(self, interface_id, enabled):
        warnings.warn("Deprecated, use set_interface_lldp_state(interface_id, enabled) instead")
        return self.set_interface_lldp_state(interface_id, enabled)