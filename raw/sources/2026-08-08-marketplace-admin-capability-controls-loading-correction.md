# Marketplace Admin Capability, Controls, And Loading Correction

Date: 2026-08-08
Author: User

The marketplace Admin UI must not show sidebar sections whose corresponding marketplace capability is disabled. Organization access remains a normal table page with a searchable header. Adding an organization is an explicit button action that opens a modal where the administrator selects an organization and grants marketplace access.

Table/list headers must expose only one refresh action. Marketplace cards, organization access, Business Products, Direct Orders, and marketplace Settings must show layout-appropriate skeletons while their data is loading; existing Products, Orders, Categories, and Category Tree loaders remain in use.

This correction applies independently per selected marketplace. For example, a Business Products + Direct marketplace must not show Marketplace Products or Marketplace Orders, while a Marketplace Products + Bidding marketplace must not show Business Products or Direct Orders.
